# PyTLDR
The Python package for connecting to and using the TLDR API

## Usage
```python
from PyTLDR import tldrify

text = tldrify(filename="PyTLDR/SampleText.pdf", ratio=0.125)
print(text)
```

This code summarizes the sample .pdf file to 0.125% of its original contents. The result will look something like this:
> Aliquam vehicula, nulla id aliquet mollis, urna elit sagittis enim, a dignissim nibh risus eget lorem.
Aenean tincidunt, augue ut sollicitudin vehicula, nunc enim dapibus velit, vitae placerat elit quam non ipsum.
Quisque ultrices, risus aliquam luctus tempus, nibh lorem volutpat quam, mollis ornare velit mauris sit amet augue.
Sed condimentum, leo sit amet hendrerit interdum, augue diam luctus dolor, commodo finibus tortor risus nec quam.

The `tldrify` function takes 5 arguments, which are technically optional, but you require exactly 2, which are listed in the Docsting:
> Returns a string summary of the input data via TLDR platform (http://tldr.pythonanywhere.com)
> Note that input text MUST be longer than once sentence to summarize
> 
> Please use one of the following:
>
> _Parameter_ url: The URL of the page to summarize. Note that this is not available at this time!
>
> _Parameter_ text: The string text to summarize. 
>
> _Parameter_ filename: The path of the file to summarize. Note that this must be .pdf, .txt, .docx, or .pptx
> 
> And one of the following:
>
> _Parameter_ ratio: The percent to shrink the data to (ex, 5 reduces the text to 5% of what it is)
>
> _Parameter_ words: The approximate word count of the resultant data
>
> _Returns_: A string summary of the data
