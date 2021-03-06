# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ...testing import assert_equal
from ..io import FreeSurferSource


def test_FreeSurferSource_inputs():
    input_map = dict(hemi=dict(usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    subject_id=dict(mandatory=True,
    ),
    subjects_dir=dict(mandatory=True,
    ),
    )
    inputs = FreeSurferSource.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_FreeSurferSource_outputs():
    output_map = dict(BA_stats=dict(altkey='BA',
    loc='stats',
    ),
    T1=dict(loc='mri',
    ),
    annot=dict(altkey='*annot',
    loc='label',
    ),
    aparc_a2009s_stats=dict(altkey='aparc.a2009s',
    loc='stats',
    ),
    aparc_aseg=dict(altkey='aparc*aseg',
    loc='mri',
    ),
    aparc_stats=dict(altkey='aparc',
    loc='stats',
    ),
    aseg=dict(loc='mri',
    ),
    aseg_stats=dict(altkey='aseg',
    loc='stats',
    ),
    brain=dict(loc='mri',
    ),
    brainmask=dict(loc='mri',
    ),
    curv=dict(loc='surf',
    ),
    curv_stats=dict(altkey='curv',
    loc='stats',
    ),
    entorhinal_exvivo_stats=dict(altkey='entorhinal_exvivo',
    loc='stats',
    ),
    filled=dict(loc='mri',
    ),
    inflated=dict(loc='surf',
    ),
    label=dict(altkey='*label',
    loc='label',
    ),
    norm=dict(loc='mri',
    ),
    nu=dict(loc='mri',
    ),
    orig=dict(loc='mri',
    ),
    pial=dict(loc='surf',
    ),
    rawavg=dict(loc='mri',
    ),
    ribbon=dict(altkey='*ribbon',
    loc='mri',
    ),
    smoothwm=dict(loc='surf',
    ),
    sphere=dict(loc='surf',
    ),
    sphere_reg=dict(altkey='sphere.reg',
    loc='surf',
    ),
    sulc=dict(loc='surf',
    ),
    thickness=dict(loc='surf',
    ),
    volume=dict(loc='surf',
    ),
    white=dict(loc='surf',
    ),
    wm=dict(loc='mri',
    ),
    wmparc=dict(loc='mri',
    ),
    wmparc_stats=dict(altkey='wmparc',
    loc='stats',
    ),
    )
    outputs = FreeSurferSource.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
