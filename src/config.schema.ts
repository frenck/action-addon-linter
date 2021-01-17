type Architecture = "aarch64" | "amd64" | "armhf" | "armv7" | "i386";

export interface Config {

  /**
   * @default false
   */
  advanced?: boolean;

  /**
   * @default true
   */
  apparmor?: boolean | string;

  arch: Architecture[];

  /**
   * @default false
   */
  audio?: boolean;

  /**
   * @default false
   */
  auth_api?: boolean;

  /**
   * @default false
   */
  auto_uart?: boolean;

  /**
   * @default auto
   */
  boot?: "auto" | "manual";

  description: string;

  /**
   * @items.pattern ^(.*):(.*):([rwm]{1,3})$
   */
  devices?: string[];

  /**
   * @default false
   */
  devicetree?: boolean;

  discovery?: string[];
  
  /**
   * @default false
   */
  docker_api?: boolean;

  environment?: { [key: string]: any; };

  /**
   * @default false
   */
  full_access?: boolean;

  /**
   * @default false
   */
  gpio?: boolean;

  /**
   * @default false
   */
  hassio_api?: boolean;

  /**
   * @default default
   */
  hassio_role?: "admin" | "backup" | "default" | "homeassistant" | "manager";

  /**
   * @default false
   */
  homeassistant_api?: boolean

  /**
   * @default false
   */
  homeassistant?: boolean;

  /**
   * @default false
   */
  host_dbus?: boolean;

  /**
   * @default false
   */
  host_ipc?: boolean;

  /**
   * @default false
   */
  host_network?: boolean;

  /**
   * @default false
   */
  host_pid?: boolean;

  /**
   * @TJS-Pattern ^([a-zA-Z\-\.:\d{}]+/)*?([\-\w{}]+)/([\-\w{}]+)(:[\.\-\w{}]+)?$
   */
  image?: string;

  ingress_entry?: string;

  /**
   * @default 8099
   * @min 0
   * @max 65535
   */
  ingress_port?: number;

  /**
   * @default false
   */
  ingress?: boolean;

  /**
   * @default true
   */
  init?: boolean;

  /**
   * @default false
   */
  kernel_modules?: boolean;

  /**
   * @default false
   */
  legacy?: boolean;

  /**
   * @items.pattern ^!?(?:intel-nuc|odroid-c2|odroid-c4|odroid-n2|odroid-xu|qemuarm-64|qemuarm|qemux86-64|qemux86|raspberrypi|raspberrypi2|raspberrypi3-64|raspberrypi3|raspberrypi4-64|raspberrypi4|tinker)$
   */
  machine?: string[];

  /**
   * @items.pattern ^(config|ssl|addons|backup|share|media)(rw|ro)?$
   */
  map?: string[];

  name: string;

  /**
   * @default {}
   */
  options?: { [key: string]: any; };

  /**
   * @default true
   */
  panel_admin?: boolean;

  /**
   * @default mdi:puzzle
   * @TJS-Pattern ^mdi:*$
   */
  panel_icon?: string;

  panel_title?: string;

  ports_description?: { 
    /**
     * @min 1
     * @max 65535
     */
    [key: string]: number;
  };

  ports?: {
    /**
     * @min 1
     * @max 65535
     */
    [key: string]: number;
  };

  privileged?: "DAC_READ_SEARCH" | "NET_ADMIN" | "SYS_ADMIN" | "SYS_MODULE" | "SYS_NICE" | "SYS_PTRACE" | "SYS_RAWIO" | "SYS_RESOURCE" | "SYS_TIME";

  /**
   * @default {}
   */
  schema?: { [key: string]: any; };

  /**
   * @items.pattern ^(?P<service>mqtt|mysql):(?P<rights>provide|want|need)$
   */
  services?: string[];

  slug: string;

  snapshot_exclude?: string[];

  /**
   * @default stable
   */
  stage?: "stable" | "experimental" | "deprecated";

  /**
   * @default application
   */
  startup?: "application" | "initialize" | "once" | "services" | "system";

  /**
   * @default false
   */
  stdin?: boolean;

  /**
   * @default 10
   * @min 10
   * @max 300
   */
  timeout?: number;

  /**
   * @TJS-Pattern ^size=(\d)*[kmg](,uid=\d{1,4})?(,rw)?$
   */
  tmpfs?: string;

  /**
   * @default false
   */
  udev?: boolean;

  /**
   * @format uri-reference
   */
  url?: string;

  /**
   * @default false
   */
  usb?: boolean;

  version: string;

  /**
   * @default false
   */
  video?: boolean;

  /**
   * @TJS-Pattern ^(?:https?|\[PROTO:\w+\]|tcp):\/\/\[HOST\]:\[PORT:\d+\].*$
   */
  watchdog?: string;

  /**
   * @TJS-Pattern ^(?:https?|\[PROTO:\w+\]):\/\/\[HOST\]:\[PORT:\d+\].*$
   */
  webui?: string;
}
