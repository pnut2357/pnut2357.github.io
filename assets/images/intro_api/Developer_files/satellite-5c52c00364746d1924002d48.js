_satellite.pushAsyncScript(function(event, target, $variables){
  document.body.addEventListener('enterprise-api-lead-form', function(event) {
  if (typeof ga === 'function') {
    ga('developerspecific.send', 'event',
      event.detail.category,
      event.detail.action,
      event.detail.label,
      event.detail.value
    );
  }
  if (typeof gtag === 'function') {
    gtag('event', 'conversion', {
      'send_to': 'AW-780419404/bf8JCN7U15MBEMyCkfQC'
  	});
  }
});
});
