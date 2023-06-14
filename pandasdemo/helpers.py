def createPandasTable(df):
    df = df.drop(columns=['id'])
    df['sequence_length'] = df['sequence'].apply(len)

    for character in ['A','G','C','T','U']:
        df[character+' %'] = df['sequence'].apply(lambda seq: (seq.upper().count(character.upper()) / len(seq)) * 100)

    # Calculate isValid field (when include the letter different than A, C, G, T, U)
    
    df['isValid'] = df['sequence'].apply(lambda seq: set(seq).issubset({'A', 'G', 'C', 'T', 'U'}))
    return df

