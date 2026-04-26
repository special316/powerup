# Released under the MIT License. See LICENSE for details.
#
"""Powerup related functionality."""

from __future__ import annotations

from typing import TYPE_CHECKING
from dataclasses import dataclass

if TYPE_CHECKING:
    from typing import Sequence
    import ba


@dataclass
class PowerupMessage:
    """A message telling an object to accept a powerup.

    Category: **Message Classes**

    This message is normally received by touching a ba.PowerupBox.
    """

    poweruptype: str
    """The type of powerup to be granted (a string).
       See ba.Powerup.poweruptype for available type values."""

    sourcenode: ba.Node | None = None
    """The node the powerup game from, or None otherwise.
       If a powerup is accepted, a ba.PowerupAcceptMessage should be sent
       back to the sourcenode to inform it of the fact. This will generally
       cause the powerup box to make a sound and disappear or whatnot."""


@dataclass
class PowerupAcceptMessage:
    """A message informing a ba.Powerup that it was accepted.

    Category: **Message Classes**

    This is generally sent in response to a ba.PowerupMessage
    to inform the box (or whoever granted it) that it can go away.
    """


def get_default_powerup_distribution() -> Sequence[tuple[str, int]]:
    """Standard set of powerups."""
    return (
        ('random_bombs', 99),
        ('triple_bombs', 0), #3
        ('ice_bombs', 0),
        ('punch', 0),
        ('impact_bombs', 0),
        ('land_mines', 0), #2
        ('sticky_bombs', 0), #3
        ('shield', 0), #2
        ('health', 0), #1
        ('curse', 0),
    )
