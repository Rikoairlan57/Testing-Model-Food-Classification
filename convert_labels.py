labels = ['ayam_oreng', 'ayam_pop', "bakso_kuah", 'cumi_tepung', 'daging_rendang',"gado_gado", 'gulai_ikan', 'gulai_tumbusu',  "mie_goreng", "mie_kuah",'nasi_goreng', 'opor_ayam',"pempek", "sate_bakar",  "sayur_asam"
         "somay", "tahu_goreng", 'telur_balado', 'telur_dadar', "tempe_goreng",  ]

file_path = 'labels.txt'

with open(file_path, 'w') as file:
    for label in labels:
        file.write(label + '\n')