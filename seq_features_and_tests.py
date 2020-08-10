def number_negatives(seq):
    """Number of negative residues in a protein.
    
    Parameters
    ----------
    seq : str
        Input sequence of protein using one-letter AA code.
        
    Returns
    -------
    output : int
        Number of negative residues in the protein
    """
    seq = seq.upper()
    return seq.count('E') + seq.count('D')

def test_number_negatives_for_single_AA():
    assert number_negatives("E") == 1
    assert number_negatives("D") == 1
    
def test_number_negatives_for_empty():
    assert number_negatives("") == 0
    
def test_number_negatives_for_short_sequence():
    assert number_negatives("ACLKTTAWE") == 1
    assert number_negatives("DDDEEE") == 6
    
def test_number_negatives_for_lowercase():
    assert number_negatives("sflkjcljwe") == 1
    
