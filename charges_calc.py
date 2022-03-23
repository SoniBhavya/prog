#from read_validate_store import val_dict

kw_ranges = [range(0,3), range(2,5), range(5,26), range(25,33), range(32,41), range(41,81)]
chief_electrical_charges = [45,45,45,223,33,334]
fixed_material_cost = [2061,2061,6362,12550,14559,16915]
fixed_service_cost = [3085,6563,9110,11847,12847,13190]
cpm_ll50 = [319,319,424,529,617,983]
cpm_gt50 = [466,466,677,888,1070,1871]
feederline_cost = [0,500,1500,1500,1500,1500] #maybe this should be added at the end seperately to the installation charges

meter_security_charges = [1000,1000,3000,9000,9000,9000] #only the kw range must be checked to get the index;the value at that index in this list will be the meter security charges

#to calculate energy charges only condition to be checked is domestic or commercial
energy_sec_dom_pkw = 700
energy_sec_comm_pkw = 2000


#function to return the index of the load range so that corresponding cost can be catched
def search_index(ld):
    for i in kw_ranges:
        if ld in i:
            print('index: ',kw_ranges.index(i))
            return(kw_ranges.index(i))

#def installation_charges(load,dist):
def charge_calc(load,dist,category):
    idx = search_index(load)
    installation_charges = chief_electrical_charges[idx] + fixed_material_cost[idx] + fixed_service_cost[idx] + feederline_cost[idx]*load + (cpm_ll50[idx]*dist) if int(dist) < 50 else (cpm_gt50[idx]*dist)
    tot_meter_security_charges = meter_security_charges[idx]

    if category == "domestic":
        es_charge = energy_sec_dom_pkw * load
    else:
        es_charge = energy_sec_comm_pkw * load
    print(" installation_charges:", installation_charges)
    print("\n meter security charges:",tot_meter_security_charges)
    print("\n Energy security charges:",es_charge )
    print("\n Total charges:", installation_charges + tot_meter_security_charges + es_charge)

