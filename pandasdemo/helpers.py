def createPandasTable(df):
    df = df.drop(columns=['id'])
    df['sequence_length'] = df['sequence'].apply(len)

    for character in ['A','G','C','T','U']:
        df[character+' %'] = df['sequence'].apply(lambda seq: (seq.upper().count(character.upper()) / len(seq)) * 100)
    # Calculate isValid field
    df['isValid'] = df['sequence'].apply(lambda seq: set(seq).issubset({'A', 'G', 'C', 'T', 'U'}))
    return df

