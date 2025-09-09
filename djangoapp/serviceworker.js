const staticCacheName = "danielfortune-pwa-v" + new Date().getTime();
const filesToCache = [
    '/offline/',
    '/static/development/css/style.css',
    '/static/images/fav-emoji-160x160.png',
    '/static/images/splash-640x1136.png',
];

// Cache on install
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    )
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("danielfortune-pwa-v")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

// Serve from Cache
// self.addEventListener("fetch", event => {
//     event.respondWith(
//         caches.match(event.request)
//             .then(response => {
//                 return response || fetch(event.request);
//             })
//             .catch(() => {
//                 return caches.match('/offline/');
//             })
//     )
// });

self.addEventListener("fetch", function (event) {
    event.respondWith(
        fetch(event.request)
            .then(function (result) {
                return caches.open(staticCacheName)
                    .then(function(c) {
                        c.put(event.request.url, result.clone())
                        return result;
                    })
            })
            .catch(function(e) {
                return caches.match(event.request)
            })
    )
});