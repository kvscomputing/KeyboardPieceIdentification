import os

def split(composer, filehandler, delimiter=',', row_limit=500,
          output_name_template='SPL_%s.csv', output_path=input("Enter file path for your splits: "), keep_headers=True):
    import csv
    output_name_template = composer+'_SPL_%s.csv'
    current_piece = 1
    reader = csv.reader(filehandler, delimiter=delimiter)
    current_out_path = os.path.join(
        output_path,
        output_name_template % current_piece
    )
    current_out_writer = csv.writer(open(current_out_path, 'w', newline=''), delimiter=delimiter)
    current_limit = row_limit
    if keep_headers:
        headers = next(reader)
        current_out_writer.writerow(headers)
    for i, row in enumerate(reader):
        if i + 1 > current_limit:
            current_piece += 1
            current_limit = row_limit * current_piece
            current_out_path = os.path.join(
                output_path,
                output_name_template % current_piece
            )
            current_out_writer = csv.writer(open(current_out_path, 'w', newline=''), delimiter=delimiter)
            if keep_headers:
                current_out_writer.writerow(headers)
        current_out_writer.writerow(row)

        
def runner():
    composer_path = input("Enter composer directory: ")
    composer = input("Enter your composer: ")
    piece = 1
    path = input("Enter full file path A: ") + composer_path +"\\COMPRESSED"
    arr_txt = [x for x in os.listdir(path) if x.startswith("COM")]
    for x in arr_txt:
        file = path +'\\'+ str(x)
        split(composer+str(piece), open(file, 'r'))
        piece = piece + 1


runner()
