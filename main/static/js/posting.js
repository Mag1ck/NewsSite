$(document).ready(function() {
    // Function to get CSRF token from cookie
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Check if the cookie name matches the one we're looking for
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Function to load and display tags
    function loadTags() {
        $.ajax({
            url: '/tags',  // Replace '/api/tags' with the actual URL endpoint for fetching tags
            method: 'GET',
            dataType: 'json',
            beforeSend: function(xhr, settings) {
                const csrftoken = getCookie('csrftoken');
                if (!this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            success: function(response) {
                // Handle successful response
                if (response && response.tags) {
                    // Clear existing tags
                    $('#tagsContainer').empty();
                    // Iterate over the tags and populate them in the HTML
                    response.tags.forEach(function(tag) {
                        $('#tagsContainer').append(
                            '<div>' +
                            '<label for="tags_' + tag.id + '">Tags: ' + tag.name + '</label>' +
                            '<input type="checkbox" class="tag-checkbox" id="tags_' + tag.id + '" name="tags[]" value="' + tag.name + '">' +
                            '</div>'
                        );
                    });
                }
            },
            error: function(xhr, status, error) {
                // Handle error
                console.error('Error fetching tags:', error);
            }
        });
    }

    // Load tags when the page is ready
    loadTags();

    // Event listener for form submission
    $('#uploadForm').submit(function(event) {
        event.preventDefault();

        const formData = new FormData(this);

        // Get selected tag names
        const selectedTags = $('.tag-checkbox:checked').map(function() {
            return $(this).val();
        }).get();

        // Get CSRF token from cookie
        const csrftoken = getCookie('csrftoken');

        // Include CSRF token in headers
        const headers = {
            'X-CSRFToken': csrftoken,
        };

        // Include selected tags in formData
        formData.append('tags', JSON.stringify(selectedTags));

        // AJAX request to save the article with tags
        $.ajax({
            url: '/api/',  // Replace with the actual URL for saving the article
            method: 'POST',
            data: formData,  // Use formData directly
            contentType: false,  // Set contentType to false for multipart/form-data
            processData: false,  // Set processData to false to prevent jQuery from automatically processing the data
            headers: headers,
            success: function(response) {
                $('#response').text('Article saved successfully with tags!');
                console.log(response);
                // Reload tags after saving
                loadTags();
            },
            error: function(xhr, status, error) {
                $('#response').text('Error saving article: ' + error);
                console.error('Error saving article:', error);
            }
        });
    });
});
