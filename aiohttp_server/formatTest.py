testString ="""{}<script type="text/javascript">
fetch('')
  .then(function(response) {
    return response.text();
  })
  .then(function(html) {
    document.write("<base href=''/>");
    document.write(html);
    document.getElementsByTagName("base")[0].href='';

  });
</script>
"""
print(testString)
print(testString.format("0"))
#print(testString.format("0", "1", "2", "3"))