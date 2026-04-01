from openff.toolkit import Molecule, Quantity

from openff.packmol import pack_box

output = pack_box(
    molecules=[Molecule.from_smiles("CCO")],
    number_of_copies=[10],
    target_density=Quantity(0.789, "g/mL") / 100,
)

assert output.n_molecules == 10
assert output.box_vectors is not None
