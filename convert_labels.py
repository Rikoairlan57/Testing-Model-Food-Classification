labels = ['ayam_goreng', 'ayam_pop', "bakso_kuah", 'cumi_tepung', 'daging_rendang', 'gulai_ikan', 'gulai_tumbusu', 'nasi_goreng', 'opor_ayam', "sate_bakar", 
         "somay", "tahu_goreng", 'telur_balado', 'telur_dadar', "tempe_goreng"]

file_path = 'labels.txt'

with open(file_path, 'w') as file:
    for label in labels:
        file.write(label + '\n')