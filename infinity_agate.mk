#
# SPDX-FileCopyrightText: The Infinity-X Project
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from device makefile.
$(call inherit-product, device/xiaomi/agate/device.mk)

# The stock MiuiCamera replaces Aperture
PRODUCT_NO_CAMERA := true

# Inherit Infinity-X product
$(call inherit-product, vendor/infinity/config/common_full_phone.mk)

# Infinity-X Specific Flags
INFINITY_BUILD_TYPE := OFFICIAL
INFINITY_MAINTAINER := "akif"
TARGET_BOOT_ANIMATION_RES := 1080
WITH_GAPPS := true
TARGET_SUPPORTS_BLUR := true

PRODUCT_NAME := infinity_agate
PRODUCT_DEVICE := agate
PRODUCT_MANUFACTURER := Xiaomi
PRODUCT_BRAND := Xiaomi
PRODUCT_MODEL := 21081111RG

PRODUCT_CHARACTERISTICS := nosdcard

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildFingerprint=Redmi/agate/agate:12/SP1A.210812.016/V14.0.6.0.TKWMIXM:user/release-keys \
    DeviceProduct=agate \
    SystemName=agate
