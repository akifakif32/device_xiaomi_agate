#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'hardware/mediatek',
    'hardware/mediatek/libaedv',
    'hardware/mediatek/libion_mtk',
    'hardware/xiaomi',
    'vendor/xiaomi/mt6893-common',
]

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
}

blob_fixups: blob_fixups_user_type = {
    'vendor/lib/hw/audio.primary.mt6893.so': blob_fixup()
        .replace_needed('libalsautils.so', 'libalsautils-v30.so')
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so')
        .add_needed('libstagefright_foundation-v33.so'),
    ('vendor/lib64/hw/android.hardware.camera.provider@2.6-impl-mediatek.so', 'vendor/lib64/libmtkcam_stdutils.so'): blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so'),
    ('vendor/lib64/libSQLiteModule_VER_ALL.so', 'vendor/lib64/lib3a.flash.so', 'vendor/lib64/lib3a.ae.stat.so', 'vendor/lib64/lib3a.sensors.color.so', 'vendor/lib64/lib3a.sensors.flicker.so', 'vendor/lib64/libaaa_ltm.so'): blob_fixup()
        .add_needed('liblog.so'),
    'vendor/bin/hw/camerahalserver': blob_fixup()
        .binary_regex_replace(b'/system/lib64', b'/vendor/lib64'),
}  # fmt: skip

module = ExtractUtilsModule(
    'agate',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    add_firmware_proprietary_file=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(module, 'mt6893-common', module.vendor)
    utils.run()
