/* global $ */

$(function() {

    // Animate the initial loading of the movie tiles
    $('.movie-tile').hide().first().show("fast", function showNext() {
       $(this).next("div").show("fast", showNext);
    });

    // Pause the video when the modal is closed
    $('.hanging-close, .modal-backdrop, .modal').on('click', function (event) {
        // Remove the src so the player itself gets removed, as this is the only
        // reliable way to ensure the video stops playing in IE
        $("#trailer-video-container").empty();
    });

    // Start playing the video whenever the trailer modal is opened
    $('.movie-tile').on('click', function (event) {
        var trailerYouTubeId = $(this).attr('data-trailer-youtube-id');
        var sourceUrl = 'https://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
        $("#trailer-video-container").empty().append($("<iframe></iframe>", {
            'id': 'trailer-video',
            'type': 'text-html',
            'src': sourceUrl,
           'frameborder': 0
        }));
    });

    // Filter the content by Genre
    $('.movie-filter').on('click', function(event) {
        var $movies = $('.movie-tile');
        var filter = event.target.id;

        if (filter === 'all') {
            $movies.hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
            });
        } else {
              $movies.hide();
              $movies.filter('.' + filter).show('fast');
        }

      // Set the filter list and page title
      $('#genre-title').html((filter).replace('-', ' '));
      $('.genre-filter').html((filter).replace('-', ' ') + '<span class="caret"></span>');
    });
});

