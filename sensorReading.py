import GroveUltrasonicRanger from GroveUltrasonicRanger


    def get_distance(self):
        while True:
            dist = self._get_distance()
            if dist:
                return dist
  
def main():
    if len(sys.argv) < 2:
        print('Usage: {} pin_number'.format(sys.argv[0]))
        sys.exit(1)
 
    sonar = GroveUltrasonicRanger(int(sys.argv[1]))
 
    print('Detecting distance...')
    while True:
        print('{} cm'.format(sonar.get_distance()))
        time.sleep(1)
 
if __name__ == '__main__':
    main()