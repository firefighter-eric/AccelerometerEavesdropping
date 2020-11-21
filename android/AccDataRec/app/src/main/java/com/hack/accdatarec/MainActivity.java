package com.hack.accdatarec;

import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.res.AssetFileDescriptor;
import android.content.res.AssetManager;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.media.AudioManager;
import android.media.MediaPlayer;
import android.net.Uri;
import android.os.Bundle;
import android.os.Handler;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import com.hack.accdatarec.util.MediaManager;

import java.io.File;
import java.io.IOException;

public class MainActivity extends AppCompatActivity {

    private Button btn_start;
    private EditText et_log;
    private AssetManager assetManager;
    private MediaPlayer mMediaPlayer;
    private String[] folders = {"02"};
    private SensorManager sensorManager;
    private Sensor sensor;
    private StringBuilder X;
    private StringBuilder Y;
    private StringBuilder Z;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // Hide action bar
        ActionBar actionBar = getSupportActionBar();
        if(actionBar != null) {
            actionBar.hide();
        }
        // Initialize UI widget
        initUI();
        SensorActivity();
        // Click events
        onClickEvent();
    }

    private void initUI(){
        et_log = (EditText)findViewById(R.id.et_log);
    }

    private void onClickEvent(){
        // Start collecting data
        new Thread(new Runnable() {
            @Override
            public void run() {
                btn_start = (Button)findViewById(R.id.btn_start);
                // Start button listener
                btn_start.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        assetManager = getAssets();
//                        playAudio("02/1_02_16.wav");
                        for (String folder:folders) {
                            try {
                                String[] fileList = assetManager.list(folder);
                                for(String filename:fileList){
                                    String filepath =  folder + "/" + filename;
                                    Log.d("Main","Playing audio");
                                    playAudio(filepath);
                                    Log.d("Main","Start file saving");
                                    Log.d("Main", "X:" + X.toString());
                                }
                            } catch (IOException e) {
                                e.printStackTrace();
                            }
                        }
                    }
                });
            }
        }).start();
    }


    private void playAudio(String filepath){
        assetManager = getAssets();
        try{
            mMediaPlayer = new MediaPlayer();
            AssetFileDescriptor audioDescriptor = assetManager.openFd(filepath);
            mMediaPlayer.setAudioStreamType(AudioManager.STREAM_MUSIC);
            mMediaPlayer.setDataSource(audioDescriptor.getFileDescriptor(),
                    audioDescriptor.getStartOffset(),
                    audioDescriptor.getLength());
            mMediaPlayer.prepare();
            Log.d("Main","Start recording acc");
            onResume();
            Log.d("Sensor", "Sensor:" + X.toString());
            mMediaPlayer.start();
//            onStop();
            Log.d("Sensor", "Sensor:" + X.toString());
            Log.d("Main","End recording acc");
            Thread.sleep(1000);
            mMediaPlayer.release();
//            mMediaPlayer.setOnCompletionListener(new MediaPlayer.OnCompletionListener() {
//                @Override
//                public void onCompletion(MediaPlayer mp) {
//                    mMediaPlayer.release();
//                }
//            });
        }catch (Exception e){
            Log.e("AudioPlay",e.toString());
        }

    }

    private void SensorActivity(){
        sensorManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);
        sensor = sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);
    }

    protected void onResume() {
        super.onResume();
        X = new StringBuilder();
        Y = new StringBuilder();
        Z = new StringBuilder();
        sensorManager.registerListener(accelerometerListener, sensor, SensorManager.SENSOR_DELAY_FASTEST);
    }

    protected void onStop() {
        super.onStop();
        sensorManager.unregisterListener(accelerometerListener);
    }

    public SensorEventListener accelerometerListener = new SensorEventListener() {
        @Override
        public void onSensorChanged(SensorEvent event) {
            float x = event.values[0];
            float y = event.values[1];
            float z = event.values[2];
            X.append(x); X.append(",");
            Y.append(y); Y.append(",");
            Z.append(z); Z.append(",");
            Log.d("Sensor2", X.toString());
        }

        @Override
        public void onAccuracyChanged(Sensor sensor, int accuracy) {

        }
    };


}