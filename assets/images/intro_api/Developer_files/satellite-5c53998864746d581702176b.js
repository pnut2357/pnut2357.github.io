_satellite.pushAsyncScript(function(event, target, $variables){
  function triggerGoogleAdsPixelTracking() {
    if (!window.twtrPixelOptIn) {
        setTimeout(triggerGoogleAdsPixelTracking, 1000);
        return;
    }
    if (window.twtrPixelOptIn === 'Y') {
        (function () {
            var s = document.getElementsByTagName("script")[0];
            var b = document.createElement("script");
            b.type = "text/javascript";
            b.async = true;
            b.src = "https://www.googletagmanager.com/gtag/js?id=AW-780419404";
            s.parentNode.insertBefore(b, s);
        })();
        window.dataLayer = window.dataLayer || [];
        window.gtag = function () {
            dataLayer.push(arguments);
        }
        gtag('js', new Date());
      	gtag('config', 'AW-780419404');
    }
}
triggerGoogleAdsPixelTracking();

});
