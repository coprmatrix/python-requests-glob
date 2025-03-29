my $name = <<'EOF';
%files -n %{python_name}
%{python3_sitelib}/requests_glob-%{version}.dist-info
%{python3_sitelib}/requests_glob.py
EOF

s/%files -n %{python_name}.*/${name}/g;
