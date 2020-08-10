_satellite.pushAsyncScript(function(event, target, $variables){
  function triggerDemandbaseTracking(eloquaCallBack) {
    if (!window.twtrPixelOptIn) {
        setTimeout(triggerDemandbaseTracking, 1000);
        return;
    }
    if (window.twtrPixelOptIn === 'Y') {
        var url = 'https://api.company-target.com/api/v2/ip.json?'
        + 'key=646ae2ad94ddfdd058eea3a96f457d97'
        + '&page=' + document.location.href
        + '&page_title='+ document.title
        + '&referrer=' + document.referrer;
        var xhr = new XMLHttpRequest();
        xhr.open('GET', url, true);
        xhr.onreadystatechange = function () {
            if (xhr.readyState == 4) {
                if (xhr.status < 400 && xhr.responseText) {
                    let jsonResponse = JSON.parse(xhr.responseText);
                    var demandbase_sid = jsonResponse.demandbase_sid || '';
                    var company_name = jsonResponse.company_name || '';
                    var industry = jsonResponse.industry || '';
                    var sub_industry = jsonResponse.sub_industry || '';
                    var employee_range = jsonResponse.employee_range || '';
                    var revenue_range = jsonResponse.revenue_range || '';
                    var audience = jsonResponse.audience || '';
                    var marketing_alias = jsonResponse.marketing_alias || '';
                    var state = jsonResponse.state || '';
                    var country = jsonResponse.country || '';
                    var watch_list_account_type = (jsonResponse.watch_list && jsonResponse.watch_list.account_type) || '';
                    var watch_list_account_status = (jsonResponse.watch_list && jsonResponse.watch_list.account_status) || '';
                    var watch_list_campaign_code = (jsonResponse.watch_list && jsonResponse.watch_list.account_type) || '';
                    var watch_list_account_owner = (jsonResponse.watch_list && jsonResponse.watch_list.account_owner) || '';
                    var fortune_1000 = jsonResponse.fortune_1000 != undefined ? jsonResponse.fortune_1000.toString() : '';
                    var forbes_2000 = jsonResponse.forbes_2000 != undefined ? jsonResponse.forbes_2000.toString() : '';
                    var b2b = jsonResponse.b2b != undefined ? jsonResponse.b2b.toString() : '';
                    var b2c = jsonResponse.b2c != undefined ? jsonResponse.b2c.toString() : '';
                    var annual_sales = jsonResponse.annual_sales || '';
                    var web_site = jsonResponse.web_site || '';

                    ga('developerspecific.set', 'dimension1', demandbase_sid);
                    ga('developerspecific.set', 'dimension2', company_name);
                    ga('developerspecific.set', 'dimension3', industry);
                    ga('developerspecific.set', 'dimension4', sub_industry);
                    ga('developerspecific.set', 'dimension5', employee_range);
                    ga('developerspecific.set', 'dimension6', revenue_range);
                    ga('developerspecific.set', 'dimension7', audience);
                    ga('developerspecific.set', 'dimension8', marketing_alias);
                    ga('developerspecific.set', 'dimension9', state);
                    ga('developerspecific.set', 'dimension10', country);
                    ga('developerspecific.set', 'dimension11', watch_list_account_type);
                    ga('developerspecific.set', 'dimension12', watch_list_account_status);
                    ga('developerspecific.set', 'dimension13', watch_list_campaign_code);
                    ga('developerspecific.set', 'dimension14', watch_list_account_owner);
                    ga('developerspecific.set', 'dimension15', fortune_1000);
                    ga('developerspecific.set', 'dimension16', forbes_2000);
                    ga('developerspecific.set', 'dimension17', b2b);
                    ga('developerspecific.set', 'dimension18', b2c);
                    ga('developerspecific.set', 'dimension19', annual_sales);
                    ga('developerspecific.set', 'dimension20', web_site);

                    ga('developerspecific.send', 'event', 'DemandBase', 'OptedIn', { nonInteraction: true});

                    const eloqua_db_forms = ['GnipDSForm'];
                    let eloquaForm = document.querySelector('.f01__form');
                  if(eloquaForm && eloqua_db_forms.indexOf(eloquaForm.name) !== -1) {
                      
                      let eloqua_key_map={'industry' : 'dbindustry', 'sub_industry':'dbsubindustry',
                                          'employee_range':'dbemprange', 'revenue_range':'dbrevrange',
                                          'annual_sales':'dbannsales', 'country':'dbcountry'};

                      Object.keys(eloqua_key_map).forEach(function(key){
                        let childNode = document.createElement('input');
                        childNode.type = 'hidden';
                        childNode.name = eloqua_key_map[key];
                        childNode.value = jsonResponse[key] || '' ;
                        eloquaForm.appendChild(childNode);
                      });

                  }

                }
            }
        };

        xhr.send();
    }
}


triggerDemandbaseTracking();

});
