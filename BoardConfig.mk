#
# SPDX-FileCopyrightText: The Infinity-X Project
# SPDX-License-Identifier: Apache-2.0
#

DEVICE_PATH := device/xiaomi/agate

# OTA assert
TARGET_OTA_ASSERT_DEVICE := agate,agatein,amber

# Display
TARGET_SCREEN_DENSITY := 440

# Properties
TARGET_VENDOR_PROP += $(DEVICE_PATH)/vendor.prop
TARGET_SYSTEM_PROP += $(DEVICE_PATH)/system.prop

# Security Patch Level
VENDOR_SECURITY_PATCH := 2023-10-01

# Inherit from mt6893-common
include device/xiaomi/mt6893-common/BoardConfigCommon.mk

# Inherit the proprietary files
include vendor/xiaomi/agate/BoardConfigVendor.mk
