import bootcamp_utils

def is_valid_sequence(seq):
    """Raise exception if seq is a valid sequence."""
        
    for aa in seq:
        if aa not in bootcamp_utils.aa:
            raise RuntimeError(aa + ' is not a valid amino acid.')
    
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
    
    is_valid_sequence(seq)
            
    return seq.count('E') + seq.count('D')



def number_positives(seq):
    """Number of positive residues in a protein.
    
    Parameters
    ----------
    seq : str
        Input sequence of protein using one-letter AA code.
        
    Returns
    -------
    output : int
        Number of positive residues in the protein
    """
    seq = seq.upper()
    
    is_valid_sequence(seq)
            
    return seq.count('E') + seq.count('D')