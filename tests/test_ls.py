from lsst.ts.LinearStage.hardware import LinearStageComponent
from zaber.serial import AsciiReply
import pytest


class TestLinearStageComponent:

    @pytest.fixture(scope="class")
    def lsc(self):
        lsc = LinearStageComponent()
        return lsc

    def test_command_accepted(self, lsc):
        reply = AsciiReply("@01 0 OK IDLE -- 0 \r")
        status_dictionary = lsc.check_reply(reply)
        assert status_dictionary is True

    @pytest.mark.parametrize(
        "data, expected",
        [
            (
                "BADDATA",
                "improperly formatted or invalid data"
            ),
            (
                "AGAIN",
                "The command cannot be processed right now. "
                "The user or application should send the command again."
            ),
            (
                "BADAXIS",
                "The command was sent with an axis number greater than the number of axes available."
            ),
            (
                "BADCOMMAND",
                "The command or setting is incorrect or invalid."
            ),
            (
                "BADMESSAGEID",
                "A message ID was provided, but was not either -- or a number from 0 to 99."
            ),
            (
                "DEVICEONLY",
                "An axis number was specified when trying to execute a device only command."
            ),
            (
                "FULL",
                "The device has run out of permanent storage and cannot accept the command."
            ),
            (
                "LOCKSTEP",
                "An axis cannot be moved using normal motion commands because it is part of a lockstep group."
            ),
            (
                "NOACCESS",
                "The command or setting is not available at the current access level."
            ),
            (
                "PARKED",
                "The device cannot move because it is currently parked."
            ),
            (
                "STATUSBUSY",
                "The device cannot be parked, nor can certain settings be changed, "
                "because it is currently busy."
            )
        ])
    def test_command_reply_flag_rejected(self, lsc, data, expected):
        reply = AsciiReply("@01 0 RJ IDLE -- {0}".format(data))
        status_dictionary = lsc.check_reply(reply)
        assert status_dictionary is False

    @pytest.mark.parametrize(
        "data, expected",
        [
            ("WR", "No reference position"),
            pytest.param("--", "No Warning"),
            ("FD", "The driver has disabled itself due to overheating."),
            ("FQ", "The encoder-measured position may be unreliable. "
                "The encoder has encountered a read error due to poor sensor alignment, "
                "vibration, dirt or other environmental conditions."),
            ("FS", "Stalling was detected and the axis has stopped itself."),
            ("FT", "The lockstep group has exceeded allowable twist and has stopped."),
            ("FB", "A previous streamed motion could not be executed because it failed a precondition "
                "(e.g. motion exceeds device bounds, calls nested too deeply)."),
            ("FP", "Streamed or sinusoidal motion was terminated because an axis slipped "
                "and thus the device deviated from the requested path."),
            ("FE", "The target limit sensor cannot be reached or is faulty."),
            ("WH", "The device has a position reference, but has not been homed. "
                "As a result, calibration has been disabled."),
            ("WL", "A movement operation did not complete due to a triggered limit sensor. "
                "This flag is set if a movement operation is interrupted by a limit sensor "
                "and the No Reference Position (WR) warning flag is not present."),
            ("WP", "The saved calibration data type for the specified peripheral.serial value "
                "is unsupported by the current peripheralid."),
            ("WV", "The supply voltage is outside the recommended operating range of the device. "
                "Damage could result to the device if not remedied."),
            ("WT",
                "The internal temperature of the controller has exceeded the recommended limit for the "
                "device."),
            ("WM", "While not in motion, the axis has been forced out of its position."),
            ("NC", "Axis is busy due to manual control via the knob."),
            ("NI", "A movement operation (command or manual control) was requested "
                "while the axis was executing another movement command. "
                "This indicates that a movement command did not complete."),
            ("ND", "The device has slowed down while following a streamed motion path "
                "because it has run out of queued motions."),
            ("NU", "A setting is pending to be updated or a reset is pending."),
            ("NJ", "Joystick calibration is in progress. Moving the joystick will have no effect.")])
    def test_command_warning_flag_rejected(self, lsc, data, expected):
        reply = AsciiReply("@01 0 RJ IDLE {0} 0".format(data))
        status_dictionary = lsc.check_reply(reply)
        assert status_dictionary is False

    @pytest.mark.parametrize(
        "data, expected",
        [
            ("WR", "No reference position"),
            pytest.param("--", "No Warning"),
            ("FD", "The driver has disabled itself due to overheating."),
            ("FQ", "The encoder-measured position may be unreliable. "
                "The encoder has encountered a read error due to poor sensor alignment, "
                "vibration, dirt or other environmental conditions."),
            ("FS", "Stalling was detected and the axis has stopped itself."),
            ("FT",
                "The lockstep group has exceeded allowable twist and has stopped."),
            ("FB",
                "A previous streamed motion could not be executed because it failed a precondition "
                "(e.g. motion exceeds device bounds, calls nested too deeply)."),
            (
                "FP",
                "Streamed or sinusoidal motion was terminated because an axis slipped "
                "and thus the device deviated from the requested path."),
            ("FE", "The target limit sensor cannot be reached or is faulty."),
            ("WH", "The device has a position reference, but has not been homed. "
                "As a result, calibration has been disabled."),
            ("WL",
                "A movement operation did not complete due to a triggered limit sensor. "
                "This flag is set if a movement operation is interrupted by a limit sensor "
                "and the No Reference Position (WR) warning flag is not present."),
            ("WP",
                "The saved calibration data type for the specified peripheral.serial value "
                "is unsupported by the current peripheralid."),
            ("WV",
                "The supply voltage is outside the recommended operating range of the device. "
                "Damage could result to the device if not remedied."),
            ("WT",
                "The internal temperature of the controller has exceeded the recommended limit for the "
                "device."),
            ("WM",
                "While not in motion, the axis has been forced out of its position."),
            ("NC", "Axis is busy due to manual control via the knob."),
            ("NI", "A movement operation (command or manual control) was requested "
                "while the axis was executing another movement command. "
                "This indicates that a movement command did not complete."),
            ("ND",
                "The device has slowed down while following a streamed motion path "
                "because it has run out of queued motions."),
            ("NU", "A setting is pending to be updated or a reset is pending."),
            ("NJ",
                "Joystick calibration is in progress. Moving the joystick will have no effect.")])
    def test_command_warning_flag_accepted(self, lsc, data, expected):
        reply = AsciiReply("@01 0 OK IDLE {0} 0".format(data))
        status_dictionary = lsc.check_reply(reply)
        assert status_dictionary is True
