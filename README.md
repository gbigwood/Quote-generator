
Add this call into your `.bashrc`:

```shuf -n 1 quotes.txt | sed 's/ -- /\n\t -- /'```

Extra quotes can by adding lines in the form:
```<quote string> -- <author>```
to quotes.txt
