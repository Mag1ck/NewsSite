$(document).ready(function() {
  let page = 1;
  let isLoading = false;
  let isClicked = false;
  let currentIndex = 0;

  // Function to fetch more data from the API
  function fetchData() {
    if (!isLoading && !isClicked) {
      isLoading = true;
      $('#loader').show(); // Show loader

      // Fetch more data from the API
      $.ajax({
        url: "http://127.0.0.1:8003/api/",
        data: { 'page': page },
        success: function(response) {
          // Append new posts to the post list
          response.results.forEach(function(post) {
            let postId = post.id;
            if (!$(`.post-link[data-id="${postId}"]`).length) {
              // Create HTML elements for post
              let listItem = $('<li></li>').css({'list-style-type': 'none', 'position': 'relative', 'align-self': 'center'});
              let anchorTag = $('<a></a>').attr({'href': '/artykul/' + post.slug, 'class': 'fontstyle post-link', 'style': 'display: inline-block; position: relative; text-align: center; overflow: hidden; border-radius: 32px;', 'data-id': post.id});
              let divElement = $('<div></div>').addClass('article_text_style');
              let titleParagraph = $('<p></p>').addClass('title-text').text(post.ArticleTitle);
              let imageElement = $('<img>').css({'width': '500px', 'height': '700px', 'z-index': '0'}).attr({'src': post.image, 'alt': post.title});

              // Append elements to each other
              divElement.append(titleParagraph);
              anchorTag.append(divElement, imageElement);
              listItem.append(anchorTag);

              // Append to post list
              $('#post-list').append(listItem);
            }
          });

          // Update page number for the next request
          page++;

          isLoading = false;
          $('#loader').hide(); // Hide loader
        },
        error: function(xhr, status, error) {
          console.error('Error fetching data:', error);
          isLoading = false;
          $('#loader').hide(); // Hide loader
        }
      });
    }
  }

  // Function to handle keyboard-based scrolling
  function handleKeyboardScroll(event) {
    if (event.keyCode === 38 || event.keyCode === 40) {
      event.preventDefault();
      isClicked = true;

      if (event.keyCode === 38) {
        currentIndex = Math.max(currentIndex - 1, 0);
      } else if (event.keyCode === 40) {
        currentIndex = Math.min(currentIndex + 1, listItems.length - 1);
      }

      listItems[currentIndex].scrollIntoView({
        behavior: 'smooth',
        block: 'center', // Scroll to the center of the element
      });

      setTimeout(function () {
        isClicked = false;
      }, 200);
    } else if (event.keyCode === 116) {
      // Reload the page if F5 is pressed
      window.location.reload();
    }
  }

  // Trigger initial data fetching when the page loads
  fetchData();

  // Event listener for keyboard scrolling
  document.addEventListener('keydown', handleKeyboardScroll);

  // Event listener for scroll event
  $(window).on('scroll', function() {
    // If the user is near the bottom of the page and no other request is in progress
    if ($(window).scrollTop() >= $(document).height() - $(window).height() - 100 && !isLoading) {
      fetchData();
    }
  });

  // Update listItems after new posts are added
  $(document).ajaxComplete(function() {
    listItems = document.querySelectorAll('.listcolumnstyle li');
  });
});
