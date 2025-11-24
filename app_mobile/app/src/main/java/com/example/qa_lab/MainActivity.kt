package com.example.qa_lab

import android.os.Bundle
import android.widget.ArrayAdapter
import android.widget.Button
import android.widget.EditText
import android.widget.ListView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val input = findViewById<EditText>(R.id.noteInput)
        val btn = findViewById<Button>(R.id.addBtn)
        val listView = findViewById<ListView>(R.id.notesList)

        val notes = mutableListOf<String>()
        val adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, notes)
        listView.adapter = adapter

        // Добавление заметки
        btn.setOnClickListener {
            val text = input.text.toString()
            if (text.isNotEmpty()) {
                notes.add(text)
                adapter.notifyDataSetChanged()
                input.text.clear()
            }
        }

        // Удаление заметки (Долгое нажатие)
        listView.setOnItemLongClickListener { _, _, position, _ ->
            val removed = notes.removeAt(position)
            adapter.notifyDataSetChanged()
            Toast.makeText(this, "Удалено: $removed", Toast.LENGTH_SHORT).show()
            true
        }
    }
}
