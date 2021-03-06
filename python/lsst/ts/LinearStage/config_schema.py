import yaml


CONFIG_SCHEMA = yaml.safe_load(
    """
$schema: http://json-schema.org/draft-07/schema#
$id: https://github.com/lsst-ts/ts_LinearStage/blob/master/schema/LinearStage.yaml
# title must end with one or more spaces followed by the schema version, which must begin with "v"
title: LinearStage v2
description: Schema for LinearStage configuration files
type: object
properties:
    stage_type:
        description: Type of stage being controlled. Must be "Igus" or "Zaber"
        type: string
        default: 'Zaber'
    serial_port:
        description: USB port for the serial interface
        type: string
        default: "/dev/ttyLinearStage1"
    daisy_chain_address:
        description: The daisy-chain device address as located in the daisy chain (for Zaber Devices only)
        type: number
        default: 1
    steps_per_mm:
        description: This is approximately the amount of steps in a millimeter (for the Zaber stage only).
        type: number
        default: 8000
    socket_address:
        description: The IP address to establish a socket connection (for use with Igus Dryve v1 controllers)
        type: string
        default: "0.0.0.0"
    socket_port:
        description: >
          The network port to establish a socket connection (for use with Igus Dryve v1
          controllers)
        type: number
        default: 502

    feed_rate:
        description: >
          Distance of travel [mm] per single motor rotation (for use with Igus Dryve v1
          controllers)
        type: number
        default: 150
    maximum_stroke:
        description: Maximum travel distance (stroke) from the homed position [mm]
        type: number
        default: 1000
    homing_speed:
        description: >
          Speed to use for homing in millimeters per second [mm/s] (for use with Igus Dryve v1
          controllers)
        type: number
        default: 30.0
    homing_acceleration:
        description: >
          Acceleration to use for homing in millimeters per second squared [mm/s^2] (for use with
          Igus Dryve v1 controllers)
        type: number
        default: 20
    motion_speed:
        description: >
          Speed to use for standard travel motion in millimeters per second [mm/s] (for use with
          Igus Dryve v1 controllers)
        type: number
        default: 50.0
    motion_acceleration:
        description: >
          Acceleration to use for standard travel motion in millimeters per second squared [mm/s^2]
          (for use with Igus Dryve v1 controllers)
        type: number
        default: 25

"""
)
