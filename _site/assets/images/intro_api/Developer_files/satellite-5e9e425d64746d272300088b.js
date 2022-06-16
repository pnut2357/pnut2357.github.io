_satellite.pushBlockingScript(function(event, target, $variables){
  window.addEventListener('dtm.event', function(event) {
 var detail = event.detail;
 ga('developerspecific.send', 'event', detail.category, detail.action, detail.label, detail.value, detail.fieldsObj);
 ga('global.send', 'event', detail.category, detail.action, detail.label, detail.value, detail.fieldsObj);
});

window.addEventListener('dtm.timing', function(event) {
 var detail = event.detail;
 ga('developerspecific.send', 'timing', detail.category, detail.key, detail.label, detail.value);
});
});
