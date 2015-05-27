# html-tag-highlighter
Django project. For a given URL, fetch HTML source, display tags used, and number of times they are used. Display source HTML. When tag name is clicked, highlight the tag in HTML source view.

- Solution is implemented using Python, Django framework, Bootstrap, jQuery.
- Additional Python libraries used: 
-- Requests (for request processing), 
-- BeautifulSoup (for parsing). 

- This web app takes an URL as input. When ‘Fetch HTML Source’ button is clicked, URL is validated, HTML source is fetched, checked for content-type, parsed for HTML tags. If any errors are encountered in this process, they are displayed on the page. If there are no errors, page displays a list of all HTML tags and the number of appearances of those tags, along with the source code. Tags are displayed in descending order of number of appearances. Clicking on a tag will highlight all corresponding tags in the HTML Source section of the page.

- A sample unitest is provided in 'tags' app.
