"""Overview
===============================================================================

+----------+------------------------------------------------------------------+
| Path     | tests/PyPoE/poe/file/_data/specifications/                       |
+----------+------------------------------------------------------------------+
| Version  | 1.0.0a0                                                          |
+----------+------------------------------------------------------------------+
| Revision | $Id$                  |
+----------+------------------------------------------------------------------+
| Author   | Omega_K2                                                         |
+----------+------------------------------------------------------------------+

Description
===============================================================================

Specification used for tests

Agreement
===============================================================================

See PyPoE/LICENSE

"""

# =============================================================================
# Imports
# =============================================================================

# Python
# 3rd-party

# self
from PyPoE.poe.file.specification.fields import Field, File, Specification

# =============================================================================
# Globals
# =============================================================================

specification = Specification(
    {
        "Main.dat": File(
            fields=(
                Field(
                    name="ForeignKey",
                    type="int",
                ),
                Field(
                    name="ForeignKeyOffset",
                    type="int",
                ),
                Field(
                    name="ForeignKeyMismatch",
                    type="int",
                    key="Other.dat",
                ),
                Field(
                    name="ForeignKeyNone",
                    type="int",
                ),
                Field(
                    name="ForeignKeyCellValue",
                    type="int",
                ),
                Field(
                    name="ConstTest",
                    type="int",
                ),
            ),
        ),
        "Other.dat": File(
            fields=(
                Field(
                    name="Value",
                    type="int",
                    unique=True,
                ),
            ),
        ),
    }
)
