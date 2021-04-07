# Copyright 2019, Rasmus Sorensen <rasmusscholer@gmail.com>
"""


"""

# imports
from opentrons import labware, instruments

# metadata
metadata = {
    'protocolName': 'RS572 SAL-Origami pipetting v1',
    'author': 'Rasmus S. Sorensen <rasmusscholer@gmail.com>',
    'description': 'Pipette DNA-Origami staple strands for TR.ZZ-5nm-spaced-x60 SAL-origami pattern.',
}

# labware
plate = labware.load('96-flat', '2')
tiprack = labware.load('opentrons-tiprack-300ul', '1')

# pipettes
pipette = instruments.P300_Single(mount='left', tip_racks=[tiprack])



