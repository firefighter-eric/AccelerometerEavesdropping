package com.example.AccDataCollection.util;

import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;

import static android.content.Context.SENSOR_SERVICE;

public class Accelerometer implements SensorEventListener {
    private final SensorManager sensorManager;
    private final Sensor accelerometer;
    private AccelerationData Data;


    public Accelerometer(Context context) {
        sensorManager = (SensorManager) context.getSystemService(SENSOR_SERVICE);
        accelerometer = sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);
    }

    public void start() {
        Data = new AccelerationData();
        sensorManager.registerListener(this, accelerometer, SensorManager.SENSOR_DELAY_FASTEST);
    }

    public AccelerationData end() {
        sensorManager.unregisterListener(this);
        return Data;
    }


    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy) {

    }

    @Override
    public void onSensorChanged(SensorEvent event) {
        long t = event.timestamp;
        float x = event.values[0];
        float y = event.values[1];
        float z = event.values[2];
        Data.add(t, x, y, z);
//        Log.d("Sensor", Data.getZ());
    }
}
