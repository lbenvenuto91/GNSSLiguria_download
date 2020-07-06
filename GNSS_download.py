
from string import ascii_lowercase
import wget
import sys,os
from datetime import datetime, date, timedelta

def GNSS_download (station=['baja','loan','camn','genu','chiv','beve'],date='2020/01/01',rate=30,hour=[c for c in ascii_lowercase[:-2]],obs_type=['obs','nav','gnav']):
    '''
    Function to automatically download GNSS obs, 
    Input are:
        - name of the station: it's a <str> with the name of the station or a <list> with the 
          names of multiple stations. By default it's a <list> with all the stations of the net

        - date: yyyy/mm/dd. By default it's 2020/01/01

        - rate: <int> 1, 5 or 30 seconds. By default it's 30s

        - hour: <list> containing alphabet letters (see RINEX 2.10 name convenction for more info). 
          By default it's a <list> with letters from a to x (24 letters)

        - observation type: it's a <str> with the tipology of the file to be downloaded. 
                - obs for observation file
                - nav for GPS navigation file
                - gnav for GLONASS navigation file
            By default it's a <list> containing all those files

    '''
    
    if type(station) == str:
        if station not in ['baja','loan','camn','genu','chiv','beve']:
            print('ERROR: {} is not a valid station Regione Liguria GNSS Network'.format(station))
            return
    elif type(station) == list :
        if all(isinstance(item, str) for item in station):
            for s in station:
                if s not in ['baja','loan','camn','genu','chiv','beve']:
                    print('ERROR: {} is not a valid station in Regione Liguria GNSS Network'.format(s))
                    return    
        else:
            print('ERROR: all element in station must be a <str> \nat least one element in {} is not a <str>'.format(station))
            return
    elif type(station) != list or type(station) != str:
        print('ERROR: station must be a <str> or a <list>, {} is a {}'.format(station,type(station)))
        return
    
    tempo=datetime(int(date[0:4]),int(date[5:7]),int(date[8:10]))
    print(tempo.strftime('%j'))

    if type(obs_type) == str:
        if obs_type not in ['obs','nav','gnav']:
            print('ERROR: {} is not a valid observation type'.format(obs_type))
            return
    elif type(obs_type) == list :
        if all(isinstance(item, str) for item in obs_type):
            for o in obs_type:
                if o not in ['obs','nav','gnav']:
                    print('ERROR: {} is not a valid observation type'.format(s))
                    return    
        else:
            print('ERROR: all element in obs_type must be a <str> \nat least one element in {} is not a <str>'.format(obs_type))
            return
    elif type(obs_type) != list or type(obs_type) != str:
        print('ERROR: obs_type must be a <str> or a <list>, {} is a {}'.format(obs_type,type(obs_type)))
        return


    if rate == 30 or rate == 5:
        print('you can only download daily data so hour input will be ignored')

        if type(station) == str and type(obs_type)==str:
            print('no loop') 
            if obs_type=='obs':
                link='http://gnss.regione.liguria.it/data/{}/rinex/{}sec/{}/{}{}0.{}d.Z'.format(station.upper(),rate,date,station,tempo.strftime('%j'),str(tempo.year)[0:2])
            elif obs_type=='nav':
                link='http://gnss.regione.liguria.it/data/{}/rinex/{}sec/{}/{}{}0.{}n.Z'.format(station.upper(),rate,date,station,tempo.strftime('%j'),str(tempo.year)[0:2])
            elif obs_type=='gnav':
                link='http://gnss.regione.liguria.it/data/{}/rinex/{}sec/{}/{}{}0.{}g.Z'.format(station.upper(),rate,date,station,tempo.strftime('%j'),str(tempo.year)[0:2])
            print(link)
        
        elif type(station) == list and type(obs_type)==str:
            print('loop on stations')
            for s in station:
                if obs_type=='obs':
                    link='http://gnss.regione.liguria.it/data/{}/rinex/{}sec/{}/{}{}0.{}d.Z'.format(s.upper(),rate,date,s,tempo.strftime('%j'),str(tempo.year)[0:2])
                elif obs_type=='nav':
                    link='http://gnss.regione.liguria.it/data/{}/rinex/{}sec/{}/{}{}0.{}n.Z'.format(s.upper(),rate,date,s,tempo.strftime('%j'),str(tempo.year)[0:2])
                elif obs_type=='gnav':
                    link='http://gnss.regione.liguria.it/data/{}/rinex/{}sec/{}/{}{}0.{}g.Z'.format(s.upper(),rate,date,s,tempo.strftime('%j'),str(tempo.year)[0:2])
                print(link)
        elif type(station) == str and type(obs_type)==list:
            print('loop on obs_types')

        elif type(station)==list and type(obs_type)==list:
            print('loop on stations and obs_types')




    elif rate == 1:
        print('you can download hourly data')
    else:
        print('ERROR: rate not supported')
        return


    
    
    



inizio=datetime(year=2020,month=6,day=1)

fine=datetime(year=2020,month=6,day=5)
data_tbd=f'{inizio.year:04}/{inizio.month:02}/{inizio.day:02}'
GNSS_download(['genu','camn'],data_tbd,30,'a','gnav')
sys.exit()
while inizio<=fine:
    data_tbd=f'{inizio.year:04}/{inizio.month:02}/{inizio.day:02}'

    
    


    inizio+=timedelta(days=1)