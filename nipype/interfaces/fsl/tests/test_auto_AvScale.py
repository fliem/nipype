# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.fsl.utils import AvScale
def test_AvScale_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    args=dict(argstr='%s',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    output_type=dict(),
    mat_file=dict(position=0,
    argstr='%s',
    ),
    )
    inputs = AvScale.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_AvScale_outputs():
    output_map = dict(average_scaling=dict(),
    determinant=dict(),
    backward_half_transform=dict(),
    forward_half_transform=dict(),
    scales=dict(),
    left_right_orientation_preserved=dict(),
    skews=dict(),
    rotation_translation_matrix=dict(),
    )
    outputs = AvScale.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value