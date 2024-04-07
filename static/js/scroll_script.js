document.addEventListener('DOMContentLoaded', function() {
    var feeds = document.querySelectorAll('.lecture-feed, .test-feed');

    feeds.forEach(function(feed) {
        var items = feed.querySelectorAll('.lecture-item, .test-item');
        var currentIndex = 0;
        var itemWidth = items[0].offsetWidth + 10;

        function changeItem(event) {
            var direction = event.clientX < feed.getBoundingClientRect().left + feed.offsetWidth / 2 ? -1 : 1;
            currentIndex = (currentIndex + direction + items.length) % items.length;
            feed.scrollTo({
                left: itemWidth * currentIndex,
                behavior: 'smooth'
            });
        }

        feed.addEventListener('click', changeItem);
    });
});

