{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "taken-input",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'RPi'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-16d0f104a295>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mRPi\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mGPIO\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mGPIO\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mtime\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mpwn_pin\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m18\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0mGPIO\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msetmode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mGIPO\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mBCM\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'RPi'"
     ]
    }
   ],
   "source": [
    "import RPi.GPIO as GPIO\n",
    "import time\n",
    "\n",
    "pwn_pin = 18\n",
    "GPIO.setmode(GIPO.BCM)\n",
    "GPIO.setup(pwm_pin, GPIO.OUT)\n",
    "pwm = GPIO.PWM(pwm_pin, 100)\n",
    "angle = 4\n",
    "pwm.start(angle)\n",
    "\n",
    "while True:\n",
    "    if time == 0: #시간 체크\n",
    "        angle=180\n",
    "    if angel < 4:\n",
    "        angle = 4\n",
    "    elif angle > 23:\n",
    "        angle = 23\n",
    "        pwm=ChangeDutyCycle(angle)\n",
    "        \n",
    "#웹서버로 현재시간 전송"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "exclusive-customs",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
