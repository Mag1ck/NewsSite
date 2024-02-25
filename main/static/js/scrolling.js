$(document).ready(function() {
  let page = 1; // Początkowa strona paginacji
  let isLoading = false; // Flag, aby nie wykonywać kolejnych zapytań, kiedy jedno jest w trakcie
  let isClicked = false; // Flag, aby obsłużyć logikę kliknięć (jeśli potrzebna)
  let currentIndex = 0; // Bieżący indeks dla obsługi nawigacji klawiaturą
  let listItems = document.querySelectorAll('.listcolumnstyle li'); // Lista elementów
  let apiUrl = "http://127.0.0.1:8000/api/"; // Startowy URL API

  // Funkcja tworząca element HTML dla posta
  function createPostElement(post) {
    let listItem = $('<li></li>', {
      css: {
        'list-style-type': 'none',
        'position': 'relative',
        'align-self': 'center'
      }
    });

    let anchorTag = $('<a></a>', {
      href: '/artykul/' + post.slug,
      class: 'fontstyle post-link',
      css: {
        'display': 'inline-block',
        'position': 'relative',
        'text-align': 'center',
        'overflow': 'hidden',
        'border-radius': '32px'
      },
      'data-id': post.id
    });

    let divElement = $('<div></div>', {
      class: 'article_text_style'
    });

    let titleParagraph = $('<p></p>', {
      class: 'title-text',
      text: post.ArticleTitle
    });

    let imageElement = $('<img>', {
      css: {
        'width': '500px',
        'height': '700px',
        'z-index': '0'
      },
      src: post.image,
      alt: post.title
    });

    divElement.append(titleParagraph);
    anchorTag.append(divElement, imageElement);
    listItem.append(anchorTag);

    return listItem;
  }

  // Funkcja do pobierania danych z API
  function fetchData() {
    if (!isLoading) {
      isLoading = true;
      $('#loader').show(); // Pokaż loader

      $.ajax({
        url: apiUrl,
        success: function(response) {
          // Sprawdzenie, czy odpowiedź zawiera pole 'results'
          let posts = response.results ? response.results : response;

          if (Array.isArray(posts)) {
            posts.forEach(function(post) {
              let postId = post.id;
              if (!$(`.post-link[data-id="${postId}"]`).length) {
                $('#post-list').append(createPostElement(post));
              }
            });

            if (response.next) {
              apiUrl = response.next;
            } else if (!response.results && page < posts.length) {
              page++;
              apiUrl = `http://127.0.0.1:8000/api/?page=${page}`;
            } else {
              $(window).off('scroll');
            }
          } else {
            console.error('Odpowiedź z API nie jest poprawną tablicą obiektów.');
          }

          isLoading = false;
          $('#loader').hide();
        },
        error: function(xhr, status, error) {
          alert('Error fetching data: ' + error);
          isLoading = false;
          $('#loader').hide();
        }
      });
    }
  }

  // Funkcja do obsługi przewijania klawiaturą
  function handleKeyboardScroll(event) {
    if (event.keyCode === 38 || event.keyCode === 40) {
      event.preventDefault();
      isClicked = true;

      let listItemsArray = Array.from(listItems);
      if (event.keyCode === 38) { // Góra
        currentIndex = Math.max(currentIndex - 1, 0);
      } else if (event.keyCode === 40) { // Dół
        currentIndex = Math.min(currentIndex + 1, listItemsArray.length - 1);
      }

      listItemsArray[currentIndex].scrollIntoView({
        behavior: 'smooth',
        block: 'center',
      });

      setTimeout(() => { isClicked = false; }, 200);
    } else if (event.keyCode === 116) {
      window.location.reload();
    }
  }

  // Inicjalizacja nasłuchiwania zdarzeń
  function initEventListeners() {
    document.addEventListener('keydown', handleKeyboardScroll);
    $(window).on('scroll', function() {
      if ($(window).scrollTop() >= $(document).height() - $(window).height() - 100 && !isLoading) {
        fetchData();
      }
    });
    $(document).ajaxComplete(function() {
      listItems = document.querySelectorAll('.listcolumnstyle li');
    });
  }

  fetchData();
  initEventListeners();
});
