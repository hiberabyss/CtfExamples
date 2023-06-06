#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Hongbo Liu <lhbf@qq.com>
# Date  : 2023-06-05 23:49:28

from z3 import *

local_50 = BitVec('local_50', 8)
local_50_1_1_ = BitVec('local_50_1_1_', 8)
local_50_2_1_ = BitVec('local_50_2_1_', 8)
local_50_3_1_ = BitVec('local_50_3_1_', 8)
local_50_4_1_ = BitVec('local_50_4_1_', 8)
local_50_5_1_ = BitVec('local_50_5_1_', 8)
local_50_6_1_ = BitVec('local_50_6_1_', 8)
local_50_7_1_ = BitVec('local_50_7_1_', 8)

local_58 = BitVec('local_58', 8)
local_58_1_1_ = BitVec('local_58_1_1_', 8)
local_58_2_1_ = BitVec('local_58_2_1_', 8)
local_58_3_1_ = BitVec('local_58_3_1_', 8)
local_58_4_1_ = BitVec('local_58_4_1_', 8)
local_58_5_1_ = BitVec('local_58_5_1_', 8)
local_58_6_1_ = BitVec('local_58_6_1_', 8)
local_58_7_1_ = BitVec('local_58_7_1_', 8)

s = Solver()

s.add(local_50_5_1_ == ord('_'))

s.add(((local_50_7_1_ + local_50_3_1_) - local_58_5_1_) - local_50_2_1_ == 0x37)

# bVar3 = (((int)local_50_7_1_ + (int)local_50_3_1_) - (int)local_58_5_1_) - (int)local_50_2_1_ == 0x37;

s.add((local_58_6_1_ - local_50_5_1_) - local_50_3_1_ * local_50_6_1_ == -0x12e3)
s.add((local_58_5_1_ + local_58_4_1_) - local_58_7_1_ * local_58_3_1_ == -0x2a7f)
s.add(local_50_7_1_ + local_50_1_1_ * local_50_2_1_ == 0x12ac)
s.add(local_58_6_1_ * local_50 - local_58_7_1_ == 0x29d1)
s.add(local_58_1_1_ - local_50_7_1_ * local_58_2_1_ * local_50_3_1_ == -0x150461)
s.add(local_50_5_1_ * local_58_1_1_ * local_50_5_1_ - local_58 == 0x10efd5)
s.add(local_50_1_1_ + local_58_2_1_ + local_50_7_1_ == 0x150)
s.add((local_50_7_1_ + local_58_3_1_ + local_50_7_1_) - local_58 == 0xf9)
s.add(local_50 + (local_58_4_1_ - local_58) == 0x74)
s.add(local_50 + local_58_2_1_ * local_50_5_1_ == 0x2b73)
s.add(local_58_3_1_ + (local_58_6_1_ - local_50_7_1_) == 0x51)
s.add(local_50_5_1_ + local_50_4_1_ + local_58_5_1_ + local_50_7_1_ == 0x182)
s.add((local_58 - local_50_2_1_) - local_50 == -0x32)
s.add(local_50_3_1_ + ((local_58 - local_50_1_1_) - local_58_7_1_) == -8)
s.add((local_50_7_1_ + local_58_6_1_ + local_58_3_1_) - local_58_4_1_ == 0xd8)
s.add((local_50_4_1_ - local_50) - local_50_6_1_ * local_58_6_1_ == -0x1520)
s.add(local_58_5_1_ + (local_58_7_1_ - local_58) == 0x7c)
s.add(local_50 * local_50_7_1_ + local_50_1_1_ == 0x32aa)
s.add(local_58 + (local_50_1_1_ - local_50_5_1_) == 0x66)
s.add((local_50_7_1_ - local_58_3_1_) - local_58_1_1_ * local_50_1_1_ == -0x2d8d)
s.add(local_50_1_1_ + local_50_4_1_ * local_58_5_1_ == 0x1707)
s.add((local_58_6_1_ + local_50 + local_58_4_1_) - local_58_5_1_ == 0xcf)
s.add(local_58_6_1_ + local_58_2_1_ * local_50_7_1_ == 0x390d)
s.add(local_50_1_1_ * local_50_5_1_ * local_50_4_1_ + local_50_7_1_ == 0x6e32f)
s.add(local_58_2_1_ + (local_58_4_1_ - local_50_5_1_ * local_50_1_1_) == -0x225a)
s.add(local_50_3_1_ + (local_50_4_1_ - local_58_7_1_) == 0x23)
s.add((local_50 - local_58_4_1_) - local_58_5_1_ == -0x80)
s.add(local_50_2_1_ * (1 - local_50_3_1_) == -0x11fe)
s.add(local_50_4_1_ - local_58_4_1_ * local_58_1_1_ == -0x370f)
s.add(local_50_2_1_ + local_50_5_1_ + local_50 + local_50_4_1_ == 0x129)

print(s.check())
res = s.model()
# print(s.model())

array = [
  res[local_58],
  res[local_58_1_1_],
  res[local_58_2_1_],
  res[local_58_3_1_],
  res[local_58_4_1_],
  res[local_58_5_1_],
  res[local_58_6_1_],
  res[local_58_7_1_],
  res[local_50],
  res[local_50_1_1_],
  res[local_50_2_1_],
  res[local_50_3_1_],
  res[local_50_4_1_],
  res[local_50_5_1_],
  res[local_50_6_1_],
  res[local_50_7_1_],
]

print(array)

# print(s)
