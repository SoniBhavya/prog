from typing import Dict

while True:

    val_dict: Dict[str, None] = {"applied_load": None, "conn_cat": None, "dist_from_source": None}

    def validate_vals(val, var_name):
        if var_name == "applied_load" or var_name == "dist_from_source":
            if val.isnumeric():
                storage(val,var_name)
            else:
                val = input("ReEnter load:\n")
                validate_vals(val, var_name)

        elif var_name == "conn_cat":
            if val.isalpha() == False:
                print('character value required')
                val = input("ReEnter connection category:")
                validate_vals(val, var_name)
            else:
                storage(val, var_name)

        return

    def storage(validated_var, key_name):
            val_dict[key_name] = validated_var
            print("stored values:", val_dict)

    applied_load = input("Enter Load:\n")
    validate_vals(applied_load, 'applied_load')

    connection_category = input("Enter connection category:\n")
    validate_vals(connection_category,'conn_cat')

    dist_from_source = input("Enter distance:\n")
    validate_vals(dist_from_source,'dist_from_source')



