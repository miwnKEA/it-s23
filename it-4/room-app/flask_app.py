from flask import Flask, render_template, redirect

app = Flask(__name__)

rooms = [
    {
        'id': 1,
        'name': 'Room 1',
        'image': 'https://randomthoughtsofaparttimelostsoul.com/wp-content/uploads/2018/04/old-persons-living-room-v5.jpg',
        'patient_id': 12345,
        'data': [65, 59, 22, 25, 56, 30, 40]
    },
    {
        'id': 2,
        'name': 'Room 2',
        'image': 'https://askahousecleaner.com/wp-content/uploads/2016/04/Elderly-persons-living-room.jpg',
        'patient_id': 12245,
        'data': [35, 25, 10, 20, 56, 100, 40]
    },
    {
        'id': 3,
        'name': 'Room 3',
        'image': 'https://i.pinimg.com/originals/e6/ff/1d/e6ff1dbcfb0737c15c9286b52e13993d.jpg',
        'patient_id': 12422,
        'data': [98, 59, 85, 82, 51, 78, 51]
    },
    {
        'id': 4,
        'name': 'Room 4',
        'image': 'https://homemadehandmade.files.wordpress.com/2013/02/living-room-old.jpg',
        'patient_id': 13251,
        'data': [65, 59, 80, 81, 56, 55, 40]
    },
    {
        'id': 5,
        'name': 'Room 5',
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkxaPQQR62XGM3NZhoRmoIX-VFhv-O3ewr5g&usqp=CAU',
        'patient_id': 14425,
        'data': [80, 96, 80, 102, 56, 71, 52]
    }, 
    {
        'id': 6,
        'name': 'Room 6',
        'image': 'https://www.aboutmanchester.co.uk/wp-content/uploads/2016/12/img_7575.jpg',
        'patient_id': 12512,
        'data': [75, 92, 80, 81, 56, 102, 40]
    }
]

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', rooms=rooms)

@app.route('/room/<room_id>', methods=['GET'])
def page(room_id):
    # loop through rooms to find the room with the given id
    for room in rooms:
        if room['id'] == int(room_id):
            return render_template('page.html', room_id=room_id, room=room)
    return redirect('/')

if __name__ == '__main__':
    app.run()
