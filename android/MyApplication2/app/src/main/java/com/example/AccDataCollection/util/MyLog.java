package com.example.AccDataCollection.util;

import android.app.Activity;
import android.view.View;
import android.widget.TextView;

import com.example.AccDataCollection.R;

import java.util.LinkedList;

public class MyLog {
    private static LinkedList<String> logs;
    private static Activity activity;
    private static View view;

    public static void setView(Activity a, View v) {
        activity = a;
        view = v;
        logs = new LinkedList<>();
    }

    public static void append(String string) {
        if (logs.size() >= 5) {
            logs.pollFirst();
        }
        logs.addLast(string);
        StringBuilder text = new StringBuilder();
        for (String log : logs) {
            text.append(log).append("\n");
        }

        activity.runOnUiThread(new Runnable() {
                                   @Override
                                   public void run() {
                                       TextView textView = view.findViewById(R.id.textview_log);
                                       textView.setText(text.toString());
                                   }
                               }
        );
    }
}
