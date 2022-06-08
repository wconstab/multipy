# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

result = "package_c"


class PackageCObject:
    __slots__ = ["obj"]

    def __init__(self, obj):
        self.obj = obj

    def return_result(self):
        return result
