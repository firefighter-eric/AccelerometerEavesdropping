package com.example.AccDataCollection.util;

import android.content.Context;
import android.content.res.AssetFileDescriptor;
import android.content.res.AssetManager;
import android.media.MediaPlayer;

import java.io.IOException;

public class Audio implements Runnable {
    private MediaPlayer mediaPlayer;
    private AssetFileDescriptor assetFileDescriptor;
    private AssetManager assetManager;
    private String fileName;

    public Audio(Context context) {
        assetManager = context.getAssets();
        mediaPlayer = new MediaPlayer();
    }

    public void setFileName(String fileName) {
        mediaPlayer.reset();
        this.fileName = fileName;
        try {
            assetFileDescriptor = assetManager.openFd(fileName);
            mediaPlayer.setDataSource(assetFileDescriptor.getFileDescriptor(),
                    assetFileDescriptor.getStartOffset(),
                    assetFileDescriptor.getLength());
            mediaPlayer.prepare();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void run() {
        mediaPlayer.start();
    }
}
