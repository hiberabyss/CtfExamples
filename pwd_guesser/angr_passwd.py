#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Hongbo Liu <lhbf@qq.com>
# Date  : 2023-06-05 16:30:20

import angr
import claripy

prog = "./a.out"
proj = angr.Project(prog, main_opts = {'base_addr': 0x100000})
# proj = angr.Project(prog)

passwd_len = 0x11

# passwd = claripy.BVS('sym_passwd', 0x10 * 8)
passwd_chars = [claripy.BVS('byte_%d' % i, 8) for i in range(passwd_len)]

initial_state = proj.factory.entry_state(args=[prog, "/tmp/passwd_file"],
                                         add_options={angr.options.LAZY_SOLVES})

# passwd = claripy.Concat(*passwd_chars + [claripy.BVV('\0', 8)])
# passwd = claripy.Concat(*passwd_chars)
passwd = claripy.BVS('mypasswd', 0x10 * 8)

# for byte in passwd_chars[:-1]:
#   initial_state.solver.add(byte >= 0x20)
#   initial_state.solver.add(byte <= 0x7e)

# initial_state.solver.add(passwd[-1] == 0)

passwd_file = angr.SimFile("sim_passwd_file", content = passwd.concat(claripy.BVV('\0')), size = 0x11)
# passwd_file = angr.SimFile("sim_passwd_file", content = 'aaaaaaaaaaaaaaaa\0', size = 0x11)
passwd_file.set_state(initial_state)
initial_state.fs.insert('/tmp/passwd_file', passwd_file)

assert initial_state.fs.get('/tmp/passwd_file') is passwd_file

incorrect_addr = 0x100f44
wrong_len = 0x100998
invalid_file = 0x100950

sim_manager = proj.factory.simulation_manager(initial_state)
sim_manager.explore(find=[incorrect_addr, invalid_file])

for i, state in enumerate(sim_manager.found):
  print('state %d @ %#x' % (i, state.addr))
  eval_input = state.solver.eval(passwd, cast_to=bytes)
  print('  concretized input: %s (length = %d)' % (eval_input, len(eval_input)))
