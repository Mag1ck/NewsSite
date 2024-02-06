document.addEventListener('DOMContentLoaded', function () {
  var isClicked = false;
  var listItems = document.querySelectorAll('.listcolumnstyle li');
  var currentIndex = 0;

  document.addEventListener('keydown', function (event) {
    if (event.keyCode === 38 || event.keyCode === 40) {
      event.preventDefault();
    }

    if (!isClicked) {
      isClicked = true;

      if (event.keyCode === 38) {
        currentIndex = Math.max(currentIndex - 1, 0);
      } else if (event.keyCode === 40) {
        currentIndex = Math.min(currentIndex + 1, listItems.length - 1);
      } else if (event.keyCode === 116) {
        window.location.reload();
      }

      listItems[currentIndex].scrollIntoView({
        behavior: 'smooth',
        block: 'center', // Scroll to the center of the element
      });

      setTimeout(function () {
        isClicked = false;
      }, 200);
    }
  });
});
