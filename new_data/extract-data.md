# Prompt for Text Extraction
´´´

1. **Format**: Extract words in the following format:
   

<word in Spanish> | <translation in Swedish>


2. **Include Prepositions**: Make sure to include prepositions that clarify the gender of nouns.

3. **Translation Requirement**: If a Swedish translation is missing, generate one.

4. **Spelling Corrections**: Correct any spelling errors in the words, but list the unmodified version below the corrected one:
  

<corrected word> | <translation>


5. **Normalization**: Normalize words and sentences:
   - Ensure all words are in lower case.
   - Follow grammatical rules to correct word casing.

6. **Line Separation**: Ensure that multiple different items, concepts, or sentences do not share the same line.

for example

    ¡qué bien! / ¡qué mal! | vad bra! / vad dåligt!

should become

    ¡qué bien! | vad bra!
    ¡qué mal! | vad dåligt!

however 

    hola / saludos | hej / tjena

should stay the same since they are all interchangable


7. **Categorization**: If there are clear categories, organize the words accordingly.

8. **Image Handling**: If provided with an image, first output a parsable format for the text before applying the above rules.

9. **ouput**: Please output in a raw text format where each category starts with a name. Followed by the words in that category acording to the format specified above. All words in a category should be indented with 4 spaces. Also output it in a text code block.


name of category: 
    <corrected word> | <translation>
    <corrected word> | <translation>
    <corrected word> | <translation>

name of another category: 
    <corrected word> | <translation>
    <corrected word> | <translation>
´´´
