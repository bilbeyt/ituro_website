CKEDITOR.dialog.add( 'accordionDialog', function ( editor ) {
    return {
        title: 'Configuração do Accordion',
        minWidth: 400,
        minHeight: 200,
        contents: [
            {
                id: 'tab-basic',
                label: 'Basic Settings',
                elements: [
                    {
                        type: 'text',
                        id: 'number',
                        label: 'Número de seções do accordion',
                        validate: CKEDITOR.dialog.validate.notEmpty( "Não pode ficar vazio" )
                    }
                ]
            }
        ],
        onOk: function() {
            var dialog = this;
            var sections = parseInt(dialog.getValueOf('tab-basic','number')); //Número de seções que serão criadas

            var section =   "<div class='panel panel-default'> \
                              <div class='panel-heading'> \
                                <h4 class='panel-title'> \
                                  <a data-toggle='collapse' data-parent='#accordion' href='#collapse0'> \
                                    Collapsible Group Item \
                                  </a> \
                                </h4> \
                              </div> \
                              <div id='collapse0' class='panel-collapse collapse'> \
                                <div class='panel-body'> \
                                  Content \
                                </div> \
                              </div> \
                            </div> "
            intern = ""
            for (i=0;i<sections;i++){

                old_id_href = '#collapse'.concat(i)
                new_id_href = '#collapse'.concat(i+1);
                old_id = "collapse".concat(i);
                new_id = "collapse".concat(i+1);


                section = section.replace(old_id_href,new_id_href);
                section = section.replace(old_id,new_id);

                intern = intern + section
            }

            editor.insertHtml('<div class="panel-group" id="accordion">'+ intern +'</div>');

        }
    };
});
