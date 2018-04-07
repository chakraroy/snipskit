import paho.mqtt.client as mqtt
import json
import random

# MQTT client to connect to the bus
mqtt_client = mqtt.Client()


# Subscribe to the important messages
def on_connect(client, userdata, flags, rc):
    mqtt_client.subscribe('hermes/intent/Greg:MLPMarksByName')\


# Process a message as it arrives
def on_message(client, userdata, msg):
    if (len(msg.payload) > 0) and (msg.topic == 'hermes/intent/Greg:MLPMarksByName'):
        data = json.loads(msg.payload)

        session_id = data['sessionId']
        ponyname = data['slots'][0]['value']['value']
        ponymark = mydict.get(ponyname)

        sayings = [ 'well I am sure it\'s {}'.format(ponymark), 
                    'hmmm let me think. that would be {}'.format(ponymark),
                    '{} has {} for the cutie mark'.format(ponyname, ponymark),
                    '{} isn\'t it'.format(ponymark),
                    '{}. got to be {}'.format(ponyname, ponymark)
                    ]

        say(session_id, random.choice(sayings))


def say(session_id, text):
    '''
    Print the output to the console and to the TTS engine
    '''
    print(text)
    mqtt_client.publish('hermes/dialogueManager/endSession', json.dumps({'text': text, "sessionId" : session_id}))

def lookupMarkByName(name):
    return mydict.get(name)

mydict = {  'twilight sparkle' : 'six-pointed star with five smaller stars',
            'rarity' : 'three lozenge diamonds',
            'applejack' : 'three red apples',
            'fluttershy' : 'three pink butterflies',
            'pinkie pie' : 'three balloons',
            'rainbow dash' : 'rainbow lightning bolt',
            'princess celestia' : 'eight-pointed sun',
            'princess luna' : 'night sky with crescent moon',
            'princess cadance' : 'crystal heart with two golden arches',
            'shining armor' : 'shield with three stars',
            'cheerilee' : 'three smiling flowers',
            'silver spoon' : 'spoon',
            'twist' : 'candy cane heart',
            'snails' : 'snail',
            'snips' : 'scissors',
            'mr cake' : 'three slices of carrot cake',
            'mrs cake' : 'three pink cupcakes',
            'big mcintosh' : 'half a green apple',
            'zecora' : 'spiral sun',
            'diamond tiara' : 'tiara',
            'mayor mare' : 'bill tied with a ribbon',
            'trixie' : 'wand with crescent moon',
            'hoity toity' : 'paper fan',
            'aunt orange' : 'three orange wedges',
            'uncle orange' : 'whole orange',
            'apple cobbler' : 'apple cobbler',
            'perfect pie' : 'three apple pies',
            'mr breezy' : 'fan',
            'joe' : 'doughnut',
            'rose' : 'rose',
            'lemon hearts' : 'three hearts',
            'daring do' : 'compass',
            'goldengrape' : 'two bunches of green grapes',
            'wild fire' : 'wheel with a flame tail',
            'davenport' : 'quill and sofa',
            'lily valley' : 'three white lilies',
            'morton saltworthy' : 'salt shaker',
            'starry eyes' : 'telescope',
            'octavia melody' : 'purple treble clef',
            'shooting star' : 'blue orion constellation',
            'play write' : 'three pencils',
            'snappy scoop' : 'camera',
            'cloudy quartz' : 'three rocks',
            'sheriff silverstar' : 'sheriff badge',
            'crafty crate' : 'crate',
            'cloud kicker' : 'cloud and sun',
            'dumb-bell' : 'dumbbell',
            'hoops' : 'three basketballs',
            'hondo flanks' : 'three american footballs',
            'foggy fleece' : 'ball of yarn',
            'mane moon' : 'yellow crescent moon',
            'tracy flash' : 'roll of film',
            'chocolate sun' : 'compass-type sun',
            'night light' : 'crescent moons',
            'royal pin' : 'safety pin',
            'holly dash' : 'strawberry'
}

if __name__ == '__main__':
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect('localhost', 1883)
    mqtt_client.loop_forever()