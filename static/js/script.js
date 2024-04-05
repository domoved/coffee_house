document.addEventListener('DOMContentLoaded', function() {
    var feeds = document.querySelectorAll('.lecture-feed, .test-feed');

    feeds.forEach(function(feed) {
        const items = feed.querySelectorAll('.lecture-item, .test-item');
        let currentIndex = 0;
        const itemWidth = items[0].offsetWidth + 10;

        function changeItem(event) {
            const direction = event.clientX < feed.getBoundingClientRect().left + feed.offsetWidth / 2 ? -1 : 1;
            currentIndex = (currentIndex + direction + items.length) % items.length;
            feed.scrollTo({
                left: itemWidth * currentIndex,
                behavior: 'smooth'
            });
        }

        feed.addEventListener('click', changeItem);
    });
});
