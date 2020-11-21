d = { '94CD0A':['porte_bureau','ON','true'],
      '94CD0E':['porte_bureau','OFF','true'],
      '956F0A':['porte_maison','ON','true'],
      '956F0E':['porte_maison','OFF','true'],
      '964A0A':['porte_chambre','ON','true'],
      '964A0E':['porte_chambre','OFF','true'],
      '210E0A':['porte_fenetre_maison_gauche','ON','true'],
      '210E0E':['porte_fenetre_maison_gauche','OFF','true'],
      '8E680A':['porte_fenetre_maison_droite','ON','true'],
      '8E680E':['porte_fenetre_maison_droite','OFF','true'],
      '90D50A':['fenetre_entree','ON','true'],
      '90D50E':['fenetre_entree','OFF','true'],
      '959F0A':['fenetre_cusine_gauche','ON','true'],
      '959F0E':['fenetre_cusine_gauche','OFF','true'],
      '94FA0A':['fenetre_cusine_droite','ON','true'],
      '94FA0E':['fenetre_cusine_droite','OFF','true'],
      '91160A':['fenetre_chambre_nico_1','ON','true'],
      '91160E':['fenetre_chambre_nico_1','OFF','true'],
      '947A0A':['fenetre_chambre_nico_2','ON','true'],
      '947A0E':['fenetre_chambre_nico_2','OFF','true'],
      '95550A':['porte_atelier','ON','true'],
      '95550E':['porte_atelier','OFF','true'],
      '95390A':['porte_chaufferie','ON','true'],
      '95390E':['porte_chaufferie','OFF','true'],
      '3F00C0':['telecommande_rf_1','ON','false'],
      '3F0000':['telecommande_rf_1','OFF','false'],
      '0F00C0':['telecommande_rf_2','ON','false'],
      '0F0000':['telecommande_rf_2','OFF','false'],
      '3300C0':['telecommande_rf_3','ON','false'],
      '330000':['telecommande_rf_3','OFF','false'],
      '0300C1':['telecommande_rf_4','ON','false'],
      '030000':['telecommande_rf_4','OFF','false'],
      '3C00C0':['telecommande_rf_5','ON','false'],
      '3C0000':['telecommande_rf_5','OFF','false'],
      '040415':['interupteur_lumiere_couloir','ON','false'],
      '040414':['interupteur_lumiere_couloir','OFF','false'],
      '555530':['mini_telecommande_rf','OFF','false'],
      '55550C':['mini_telecommande_rf','ON','false']
      }

p = data.get('payload')

if p is not None:
    if p in d.keys():
        service_data = {'topic':'home/{}'.format(d[p][0]), 'payload':'{}'.format(d[p][1]), 'qos':0, 'retain':'{}'.format(d[p][2])}
    else:
        service_data = {'topic':'home/unknown', 'payload':'{}'.format(p), 'qos':0, 'retain':'false'}
        logger.warning('<rfbridge_demux> Received unknown RF command: {}'.format(p))
    hass.services.call('mqtt', 'publish', service_data, False)